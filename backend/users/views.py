from django.shortcuts import render
from django.contrib.auth.views import LoginView


from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.models import Permission
from django.contrib.contenttypes.models import ContentType
from django.shortcuts import get_object_or_404
from django.views.generic import TemplateView
from .models import User
# Create your views here.
from django.views.generic import ListView


from django.contrib.auth.models import Permission
from django.urls import reverse_lazy

from rest_framework import parsers, renderers, generics, status
from rest_framework.authtoken.models import Token
from .serializers import AuthTokenSerializer, UserSerializer, UserModelSerializer, CreateUserSerializer, UserPermissionSerializer
from rest_framework.compat import coreapi, coreschema
from rest_framework.response import Response
from rest_framework.schemas import ManualSchema
from rest_framework.schemas import coreapi as coreapi_schema
from rest_framework.views import APIView
from .models import *


class AuthToken(APIView):
    throttle_classes = ()
    permission_classes = ()
    parser_classes = (parsers.FormParser, parsers.MultiPartParser, parsers.JSONParser,)
    renderer_classes = (renderers.JSONRenderer,)
    serializer_class = AuthTokenSerializer

    if coreapi_schema.is_enabled():
        schema = ManualSchema(
            fields=[
                coreapi.Field(
                    name="email",
                    required=True,
                    location='form',
                    schema=coreschema.String(
                        title="Email",
                        description="E-mail válido para autenticação.",
                    ),
                ),
                coreapi.Field(
                    name="password",
                    required=True,
                    location='form',
                    schema=coreschema.String(
                        title="Password",
                        description="Senha para autenticação.",
                    ),
                ),
            ],
            encoding="application/json",
        )

    def get_serializer_context(self):
        return {
            'request': self.request,
            'format': self.format_kwarg,
            'view': self
        }

    def get_serializer(self, *args, **kwargs):
        kwargs['context'] = self.get_serializer_context()
        return self.serializer_class(*args, **kwargs)

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

    # Check if the user is valid
        if 'user' not in serializer.validated_data:
            return Response({'error': 'Invalid user'}, status=status.HTTP_400_BAD_REQUEST)

        user = serializer.validated_data['user']
    # Check if the password is valid
        if not user.check_password(request.data.get('password')):
            return Response({'error': 'Invalid password'}, status=status.HTTP_400_BAD_REQUEST)

        user = serializer.validated_data['user']
        token, created = Token.objects.get_or_create(user=user)
        user_serializer = UserSerializer(user)
        return Response({'token': token.key, 'user': user_serializer.data})


class UserListViewAPI(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserModelSerializer


class UserCRUDViewAPI(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserModelSerializer


class UserCreateView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = CreateUserSerializer

class ManageUserPerms(APIView):
    queryset = User.objects.all()

    def post(self, request):
        serializer = UserPermissionSerializer(data=request.data)
        if serializer.is_valid():
            user_id = serializer.validated_data['user_id']
            codename = serializer.validated_data['codename']
            action = serializer.validated_data['action']
            try:
                user = User.objects.get(id=user_id)
                permission = Permission.objects.get(codename=codename)
                print(permission.codename)
                if action == 'add':
                    user.user_permissions.add(permission.codename)
                    return Response({'message' : 'Permissão {} adicionada com sucesso.'.format(permission)})
                elif action == 'remove':
                    user.user_permissions.remove(permission.codename)
                    return Response({'message' : 'Permissão {} removida com sucesso'.format(permission)})
            except User.DoesNotExist:
                return Response({'error' : 'Usuário não encontrado.'}, status=status.HTTP_400_BAD_REQUEST)
            except Permission.DoesNotExist:
                return Response({'error' : 'Permissão não encontrada.'})
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    class Meta:
        model = User
            

class ClassicLoginView(LoginView):
    template_name = 'login/login.html'

    def get_success_url(self):
        return reverse_lazy('intranet:enterprise_home')


class ManageUserPermsView(LoginRequiredMixin, TemplateView):
    template_name = 'manage_user_perms.html'

    def get_context_data(self, **kwargs):
        user_id = self.kwargs.get('user_id')
        user = get_object_or_404(User, id=user_id)
        
        # Get content type for the custom user model
        content_type = ContentType.objects.get_for_model(User)
        
        # Get all permissions related to the User model
        user_permissions = Permission.objects.filter(content_type=content_type)
        context = super().get_context_data(**kwargs)
        context['user'] = user
        context['user_permissions'] = user_permissions
        return context


class UserListView(LoginRequiredMixin, UserPassesTestMixin, ListView):
    model = User
    template_name = 'equipe/list.html'
    context_object_name = 'users'

    def test_func(self):
        return self.request.user.is_superuser  # Restrict access to staff/admin users

from bootstrap_modal_forms.generic import BSModalCreateView, BSModalReadView, BSModalUpdateView, BSModalDeleteView
from .forms import *
from django.contrib.messages.views import SuccessMessageMixin

class UserCreateModalView(BSModalCreateView,SuccessMessageMixin,LoginRequiredMixin):
    login_url = '/user/login/'
    template_name = 'generic/create.html'
    form_class = UserForm
    success_message = 'Usuário criado com sucesso.'
    success_url = reverse_lazy('users:user_list')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["modal_title"] = 'Cadastro de Usuário'
        context["hint"] = 'Realize o cadastro do usuário para que ele possa ter acesso à intranet.'

        return context
    
from django.forms.models import model_to_dict


class UserDetailView(BSModalReadView, LoginRequiredMixin):
    login_url = '/user/login/'
    template_name = 'generic/detail.html'
    model = User

    def get_context_data(self, **kwargs):
        context = {}
        context["modal_title"] = 'Visualizar de Usuário'
        context["hint"] = 'Confira os detalhes no cadastro.'
        if self.object:
            context["object"] = self.object
            context_object_name = self.get_context_object_name(self.object)
            if context_object_name:
                context[context_object_name] = self.object
                context['dict_data'] = self.object.to_dict_verbose(fields=['first_name','last_name','email','telefone'])
        
        context.update(kwargs)
        return super().get_context_data(**context)


class UserEditView(BSModalUpdateView, LoginRequiredMixin):
    login_url = '/user/login/'
    model = User
    template_name = 'generic/edit.html'
    form_class = UserForm
    success_message = 'Usuário editado com sucesso'
    success_url = reverse_lazy('users:user_list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["modal_title"] = 'Editar usuário'
        context["hint"] = '*Cuidado, você está editando um usuário do sistema.'

        return context


#########################################################################
####### AQUI É A VIEW DE REQUISIÇÃO PARA ATUALIZAÇÃO DE PASSWORD ######## 
#########################################################################

from django.views import View
from django.shortcuts import render, redirect
from django.core.mail import send_mail, EmailMultiAlternatives
from django.contrib.auth.tokens import default_token_generator
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from .models import User

class PasswordResetRequestView(View):
        
    def send_password_reset_email(self, user, reset_url):
        from_email = 'intranet@maissabor.ind.br'
        context = {
            'user': user,
            'reset_url': reset_url,
        }
        subject = 'Redefinição de Senha'
        html_content = render_to_string('login/email.html', context)
        text_content = strip_tags(html_content)  # Versão de texto para clientes de e-mail que não suportam HTML

        email = EmailMultiAlternatives(
            subject, text_content, from_email, [user.email]
        )
        email.attach_alternative(html_content, "text/html")
        email.send()
    
    def get(self, request):
        return render(request, 'login/password_reset_request.html')

    def post(self, request):
        email = request.POST.get('email')
        user = User.objects.filter(email=email).first()
        if user:
            token = default_token_generator.make_token(user)
            reset_url = request.build_absolute_uri(f"/password_reset/{user.pk}/{token}/")
            self.send_password_reset_email(user, reset_url)
        return redirect('password_reset_done')

class PasswordResetView(View):
    def get(self, request, uidb64, token):
        user = get_object_or_404(User, pk=uidb64)
        valid_token = default_token_generator.check_token(user, token)
        if not valid_token:
            return render(request, 'password_reset_invalid.html')
        return render(request, 'login/password_reset_form.html', {'user': user})

    def post(self, request, uidb64, token):
        user = get_object_or_404(User, pk=uidb64)
        new_password = request.POST.get('password')
        user.set_password(new_password)
        user.password_set = True
        user.save()
        return redirect('password_reset_complete')


##################################################################################
############## FIM DAS VIEWS DE REDEFINIÇÃO DE SENHA #############################
##################################################################################





##### DAQUI PRA BAIXO SÓ INICIALIZA AS CLASSES COMO VIEWS, NESSE CASO ELAS SÃO IMPORTADAS NA URLS COMO OBJETOS JÁ INSTANCIADOS ######




obtain_auth_token = AuthToken.as_view()
user_list = UserListView.as_view()
user_crud = UserCRUDViewAPI().as_view()
user_create = UserCreateView().as_view()
manage_perms = ManageUserPerms.as_view()
classic_login = ClassicLoginView.as_view()
manage_perms_classic = ManageUserPermsView.as_view()
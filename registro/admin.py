from django.contrib import admin
from .models import RegistroAtividade, Equipamento, Funcionario, Funcao, InspecaoEquipamento, RegistroEvento

@admin.register(RegistroAtividade)
class RegistroAtividadeAdmin(admin.ModelAdmin):
    ...

@admin.register(Equipamento)
class EquipamentoAdmin(admin.ModelAdmin ):
    ...

@admin.register(Funcionario)
class FuncionarioAdmin(admin.ModelAdmin):
    ...

@admin.register(Funcao)
class FuncaoAdmin(admin.ModelAdmin ):
    ...
@admin.register(InspecaoEquipamento)
class InspecaoEquipamentoAdmin(admin.ModelAdmin ):
    ...
    
@admin.register(RegistroEvento)
class RegistroEventoAdmin(admin.ModelAdmin ):
    ...
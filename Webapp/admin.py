from django.contrib import admin
from .models import *

# Register your models here.
class UtilisateurAdmin(admin.ModelAdmin):
    list_display = ('id', 'Nom_Complet', 'Departement', 'Fonction')

class News_PostAdmin(admin.ModelAdmin):
    list_display = ('id', 'Titre', 'Auteur_pub', 'Date_pub')
    
class Manage_StressAdmin(admin.ModelAdmin):
    list_display = ('id', 'Titre_MS', 'Description_MS', 'Date_pub_MS')

class RessourcesAdmin(admin.ModelAdmin):
    list_display = ('id', 'Titre_Ressource', 'Description_Ressource', 'Date_pub_Ressource')

class CommentairesAdmin(admin.ModelAdmin):
    list_display = ('id', 'Titre_pub', 'Auteur_Comment_pub', 'Date_Comment_pub')
    
class MessageAdmin(admin.ModelAdmin):
    list_display = ('id', 'User_send_msg', 'Object_msg', 'Date_send_msg')
    
class AssistanceAdmin(admin.ModelAdmin):
    list_display = ('id', 'Cas', 'Suivi')
    
class RoomAdmin(admin.ModelAdmin):
    list_display = ('id', 'Theme')
    
class Private_MessageAdmin(admin.ModelAdmin):
    list_display = ('id', 'User', 'Message', 'Room', 'Date')
    
admin.site.register(Utilisateur, UtilisateurAdmin)
admin.site.register(News_Post, News_PostAdmin)
admin.site.register(Manage_Stress, Manage_StressAdmin)
admin.site.register(Ressources, RessourcesAdmin)
admin.site.register(Commentaires, CommentairesAdmin)
admin.site.register(Message, MessageAdmin)
admin.site.register(Assistance, AssistanceAdmin)
admin.site.register(Room, RoomAdmin)
admin.site.register(Private_Message, Private_MessageAdmin)
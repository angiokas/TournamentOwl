from django.contrib import admin

from .models import Competitor, Debate, Judge, Score, Tournament, UserProfile


# Register the Tournament model
class TournamentAdmin(admin.ModelAdmin):
    list_display = (
        "title",
        "start_date",
        "end_date",
        "registration_deadline",
        "location",
        "created_at",
        "updated_at",
    )
    search_fields = ("title", "description", "location")
    list_filter = ("start_date", "end_date", "location")
    date_hierarchy = "start_date"


admin.site.register(Tournament, TournamentAdmin)


# Register the Debate model
class DebateAdmin(admin.ModelAdmin):
    list_display = (
        "statement",
        "start_time",
        "end_time",
        "tournament",
        "created_at",
        "updated_at",
    )
    search_fields = ("statement",)
    list_filter = ("tournament", "start_time", "end_time")
    date_hierarchy = "start_time"


admin.site.register(Debate, DebateAdmin)


# Register the UserProfile model (inheriting from the User model)
class UserProfileAdmin(admin.ModelAdmin):
    list_display = (
        "username",
        "rank",
        "email",
        "first_name",
        "last_name",
        "date_joined",
        "last_login",
    )
    search_fields = ("username", "email", "first_name", "last_name")
    list_filter = ("rank", "date_joined", "last_login")


admin.site.register(UserProfile, UserProfileAdmin)


# Register the Competitor model
class CompetitorAdmin(admin.ModelAdmin):
    list_display = ("user", "debate")
    search_fields = ("user__username", "debate__statement")
    list_filter = ("debate",)
    raw_id_fields = ("user", "debate")


admin.site.register(Competitor, CompetitorAdmin)


# Register the Judge model
class JudgeAdmin(admin.ModelAdmin):
    list_display = ("user", "debate")
    search_fields = ("user__username", "debate__statement")
    list_filter = ("debate",)
    raw_id_fields = ("user", "debate")


admin.site.register(Judge, JudgeAdmin)


# Register the Score model
class ScoreAdmin(admin.ModelAdmin):
    list_display = ("competitor", "judge", "debate", "score", "feedback")
    search_fields = (
        "competitor__user__username",
        "judge__user__username",
        "debate__statement",
    )
    list_filter = ("debate", "competitor", "judge")
    raw_id_fields = ("competitor", "judge", "debate")


admin.site.register(Score, ScoreAdmin)

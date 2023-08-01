from flask import Blueprint, redirect, render_template, request, url_for

from CTFd.constants.config import ChallengeVisibilityTypes, Configs
from CTFd.utils.config import is_teams_mode
from CTFd.utils.dates import ctf_ended, ctf_paused, ctf_started
from CTFd.utils.decorators import (
    during_ctf_time_only,
    require_complete_profile,
    require_verified_emails,
)
from CTFd.models import Certificate, Users, Teams, Challenges, db
from CTFd.utils.decorators.visibility import check_challenge_visibility
from CTFd.utils.helpers import get_errors, get_infos
from CTFd.utils.user import (
    authed,
    get_current_team,
    get_current_team_attrs,
    get_current_user,
    get_current_user_attrs,
    is_admin)

challenges = Blueprint("challenges", __name__)


@challenges.route("/challenges", methods=["GET"])
@require_complete_profile
@during_ctf_time_only
@require_verified_emails
@check_challenge_visibility
def listing():
    if (
        Configs.challenge_visibility == ChallengeVisibilityTypes.PUBLIC
        and authed() is False
    ):
        pass
    else:
        if is_teams_mode() and get_current_team() is None:
            return redirect(url_for("teams.private", next=request.full_path))

    infos = get_infos()
    errors = get_errors()

    if Configs.challenge_visibility == ChallengeVisibilityTypes.ADMINS:
        infos.append("Challenge Visibility is set to Admins Only")

    if ctf_started() is False:
        errors.append(f"{Configs.ctf_name} has not started yet")

    if ctf_paused() is True:
        infos.append(f"{Configs.ctf_name} is paused")

    if ctf_ended() is True:
        infos.append(f"{Configs.ctf_name} is ended")

    return render_template("challenges.html", infos=infos, errors=errors)
    # Certificate Generation Logic

    # certificate = Certificate(
    #     username=Users.name,
    #     ctf_name=Configs.ctf_name,
    #     team_place=Teams.place,
    #     user_place=Users.place,
    #     user_id=Users.id,
    #     team_name=Teams.name if is_teams_mode else None
    # )
    # db.session.add(certificate)

#
        # try:
        #     if is_teams_mode():
        #         teams = Teams.query.all()
        #         for team in teams:
        #             print(f"For Team: {team.name}")
        #             certificate = Certificate(
        #                 team_name=team.name,
        #                 ctf_name=Configs.ctf_name,
        #                 team_place=team.place,
        #                 team_id=team.id,
        #             )
        #             print(certificate)
        #             db.session.add(certificate)
        #             db.session.commit()
        #     else:
        #         users = Users.query.all()
        #         for user in users:
        #             print(f"For User: {user.name}")
        #             certificate = Certificate(
        #                 username=user.name,
        #                 ctf_name=Configs.ctf_name,
        #                 user_place=user.place,
        #                 user_id=user.id,
        #             )
        #             print(certificate)
        #             db.session.add(certificate)
        #             db.session.commit()
        # except:
        #     print("error in certifiae")

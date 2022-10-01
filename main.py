#!/usr/bin/python3
# -*- coding: utf-8 -*-

import os
from re import I
from jira.client import JIRA
import datetime
projects = ['MSG',]
qtde_sprints = 6
sprint_passada = 406
email_login = os.environ.get('EMAIL_JIRA')
token_login = os.environ.get('TOKEN_JIRA')
options = {'server': os.environ.get('SERVER'),}
qtde_items_current_sprint_entregues = 0
qtde_items_current_sprint_nentregues = 0
qtde_items_past_sprints_entregues = 0
qtde_items_past_sprints_nentregues = 0
qtde_items_past1_sprint_nentregues = 0
qtde_items_past1_sprint_entregues = 0
jira = JIRA(options=options, basic_auth=(email_login, token_login))
print("Mensageria - Relatório/Indicadores (Ref 2° Semestre 2022)")
print(f"Gerado às: {datetime.datetime.now()}")
for project in projects:
    #=====================================================================================================================================================
    print("[Sprint Corrente]")
    issues_done = jira.search_issues(f'project={project} and sprint in openSprints() AND resolved >= "2022-06-30 00:00" and status in ("Concluído", "done", "canceled") and type not in ("Bug em QA")', maxResults=False)
    story_point_done = 0
    for issue_current in issues_done:
        qtde_items_current_sprint_entregues+= 1
        if issue_current.fields.customfield_10032:
            story_point_done += issue_current.fields.customfield_10032
    print(f"- Story points concluídos: {story_point_done}")
    print(f"- Quantidade itens: {qtde_items_current_sprint_entregues}")
    
    issues_ndone = jira.search_issues(f'project={project} AND sprint in openSprints() AND resolution = Unresolved AND status not in ("Concluído", "done", "canceled") and type not in ("Bug em QA")', maxResults=False)
    story_point_ndone = 0
    for issue_current in issues_ndone:
        qtde_items_current_sprint_nentregues+= 1
        if issue_current.fields.customfield_10032:
            story_point_ndone += issue_current.fields.customfield_10032
    print(f"- Story points não concluídos: {story_point_ndone}")
    print(f"- Quantidade itens: {qtde_items_current_sprint_nentregues}")
   # print(f"- TOTAL ITENS: {qtde_items_current_sprint_entregues + qtde_items_current_sprint_nentregues}")
    #=====================================================================================================================================================
    #=====================================================================================================================================================
    print("[Sprint Anterior]")
    issues_done = jira.search_issues(f'project={project} AND Sprint = {sprint_passada} AND status in ("Concluído", "done", "canceled") AND resolved <= "2022-09-13 00:00" and type not in ("Bug em QA")', maxResults=False)
    story_point_past1_done = 0
    for issue_current in issues_done:
        qtde_items_past1_sprint_entregues+= 1
        if issue_current.fields.customfield_10032:
            story_point_past1_done += issue_current.fields.customfield_10032
    print(f"- Story points concluídos: {story_point_past1_done}")
    print(f"- Quantidade itens: {qtde_items_past1_sprint_entregues}")
    
    issues_ndone = jira.search_issues(f'project={project} AND Sprint = {sprint_passada} AND resolution = Unresolved AND status not in ("Concluído", "done", "canceled") and type not in ("Bug em QA")', maxResults=False)
    story_point_past1_ndone = 0
    for issue_current in issues_ndone:
        qtde_items_past1_sprint_nentregues+= 1
        if issue_current.fields.customfield_10032:
            story_point_past1_ndone += issue_current.fields.customfield_10032
    print(f"- Story points não concluídos: {story_point_past1_ndone}")
    print(f"- Quantidade itens: {qtde_items_past1_sprint_nentregues}")
    #=====================================================================================================================================================
    #=====================================================================================================================================================
    print("[Todas as Sprints Anteriores]")
    issues_done_past = jira.search_issues(f'project={project} AND sprint in closedSprints() AND resolved >= "2022-06-30 00:00" and status in ("Concluído", "done", "canceled") and type not in ("Bug em QA")', maxResults=False)
    story_point_past_done = 0
    for issue_past in issues_done_past:
        qtde_items_past_sprints_entregues += 1
        if issue_past.fields.customfield_10032:
            story_point_past_done += issue_past.fields.customfield_10032
    #sprint_past = issue.fields.customfield_10020[-1].name
    print(f"- Story points concluídos: {story_point_past_done}")
    print(f"- Quantidade itens: {qtde_items_past_sprints_entregues}")
    issues_ndone_past = jira.search_issues(f'project={project}  AND sprint in closedSprints() AND resolution = Unresolved AND updated >= "2022-06-30 00:00" and status not in ("Concluído", "done", "canceled") and type not in ("Bug em QA")', maxResults=False)
    story_point_ndone_past = 0
    for issue_past in issues_ndone_past:
        qtde_items_past_sprints_nentregues += 1
        if issue_past.fields.customfield_10032:
            story_point_ndone_past += issue_past.fields.customfield_10032
    #sprint_past = issue.fields.customfield_10020[-1].name
    print(f"- Story points não concluídos: {story_point_ndone_past}")
    print(f"- Quantidade itens: {qtde_items_past_sprints_nentregues}")
    
    #=====================================================================================================================================================
    # print("[Sprints Futura]")
    # issues_done_future = jira.search_issues(f'project={project} and sprint in futureSprints()', maxResults=3000)
    # story_point_done_future = 0
    # if issues_done_future:
    #     for issue_future in issues_done_future:
    #         if issue_future.fields.customfield_10032:
    #             story_point_done_future += issue_future.fields.customfield_10032
    #     #sprint_future = issue_future.fields.customfield_10020[-1].name
    #     print(f"Story points estimados: {story_point_done_future}")
    # else:
    #     print(f"Story points estimados: 0")
    print("[TOTAIS]")
    print(f"- Quantidade de itens concluídos (Últimos 30 dias): {qtde_items_past_sprints_entregues + qtde_items_past1_sprint_entregues}")
    print(f"- Total SP's Entregues (Últimos 30 dias): {story_point_done + story_point_past1_done}")
    print(f"- Quantidade de itens concluídos (Todo o ciclo): {qtde_items_past_sprints_entregues + qtde_items_past_sprints_nentregues}")
    print(f"- Total SP's Entregues (Todo o ciclo): {story_point_done + story_point_past_done}")
    media = (story_point_done + story_point_past_done) / qtde_sprints
    print(f"- Média SP/Sprint: {media}")

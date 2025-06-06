from agents import Agent, handoff, RunContextWrapper
import requests
from dotenv import load_dotenv, find_dotenv
import os
from agents.extensions.handoff_prompt import RECOMMENDED_PROMPT_PREFIX
from pydantic import BaseModel

from modules.modules import *


from Agents.Code.BackEnd.Keys_env.Integration import CodeFlaskBackEndSprint13Agent
from Agents.Code.BackEnd.Keys_fb.Integration import CodeFlaskBackEndSprint12Agent


class Data(BaseModel):
    Content: str

async def on_handoff(ctx: RunContextWrapper[dict], input_data: Data):
    print(f"Code Review FrontEnd JS Agent: {input_data.Content}")

def CodeReviewFrontEndJSAgent(session_id, appcompany):
    path_ProjectWeb = "/app/LocalProject"
    os.chdir(path_ProjectWeb)
    path_html = f"templates"
    path_js = f"static/js"
    path_css = f"static/css"
    doc_md = f"doc_md"

    githubtoken = os.getenv("github_username_Ualers")
    repo_owner = os.getenv("companyname")

    agent_, handoff_obj_Keys_env = CodeFlaskBackEndSprint13Agent("","")
    agent_, handoff_obj_Keys_fb = CodeFlaskBackEndSprint12Agent("","")

    name_agent, model_agent, instruction_original, tools_agent  = get_settings_agents(path_metadata = os.path.join(os.path.dirname(__file__), "metadata.json"))
    instruction_formatado = format_instruction(instruction_original, locals())

    Tools_Name_dict = Egetoolsv2(list(tools_agent))
    agent = Agent(
        name=name_agent,
        instructions = f"""
{RECOMMENDED_PROMPT_PREFIX}
{instruction_formatado}
        """
        ,
        model=str(model_agent),
        tools=Tools_Name_dict,
        handoffs=[
          handoff_obj_Keys_env,
          handoff_obj_Keys_fb
        ]
        
    )

    handoff_obj = handoff(
        agent=agent,
        on_handoff=on_handoff,
        input_type=Data,
    )
    return agent, handoff_obj
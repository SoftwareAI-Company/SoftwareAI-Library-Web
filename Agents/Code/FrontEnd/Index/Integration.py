from agents import Agent, handoff, RunContextWrapper
import requests
from dotenv import load_dotenv, find_dotenv
import os
from agents.extensions.handoff_prompt import RECOMMENDED_PROMPT_PREFIX
from pydantic import BaseModel
from modules.modules import *


from Agents.Code.FrontEnd.Transfer.Integration import CodeTransferAgent


class Data(BaseModel):
  Content: str

async def on_handoff(ctx: RunContextWrapper[dict], input_data: Data):
  print(f"CodeIndexFrontEnd: {input_data.Content}")
    
def CodeIndexFrontEnd(
      WEBHOOK_URL,
      session_id,
      user_email,
        
    ):
    agent_, handoff_obj_CodeTransferAgent = CodeTransferAgent("", "")

   
    path_ProjectWeb = "/app/LocalProject"
    os.chdir(path_ProjectWeb)
    path_html = f"{path_ProjectWeb}/templates"
    path_js = f"{path_ProjectWeb}/static/js"
    path_css = f"{path_ProjectWeb}/static/css"
    doc_md = f"{path_ProjectWeb}/doc_md"

    githubtoken = os.getenv("github_username_Ualers")
    repo_owner = os.getenv("companyname")


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
        handoffs=[handoff_obj_CodeTransferAgent],


    )



    handoff_obj = handoff(
        agent=agent,
        on_handoff=on_handoff,
        input_type=Data,
    )

    return agent, handoff_obj
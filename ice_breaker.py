from dotenv import load_dotenv
from langchain.chains.llm import LLMChain
from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
from third_parties.linkedin import scrape_linkedin_profile
from agents.linkedin_lookup_agent import lookup as linkedin_lookup_agent

if __name__ == "__main__":
    load_dotenv()

    # information = """
    # Samuel Harris Altman (born April 22, 1985) is an American entrepreneur and investor best known as the CEO of OpenAI since 2019 (he was briefly fired and reinstated in November 2023). Altman is considered to be one of the leading figures of the AI boom. He dropped out of Stanford University after two years and founded Loopt, a mobile social networking service, raising more than $30 million in venture capital. In 2011, Altman joined Y Combinator, a startup accelerator, and was its president from 2014 to 2019.
    # """

    linkedin_profile_url = linkedin_lookup_agent(name="Jeegar Shah Alexa AI CMU")

    summary_template = """
    given the LinkedIn information {information} about the person I want you to create:
    1. A short summary
    2. two interesting facts about them
    """

    summary_prompt_template = PromptTemplate(
        input_variables=["information"], template=summary_template
    )

    llm = ChatOpenAI(temperature=0, model_name="gpt-3.5-turbo")

    chain = LLMChain(llm=llm, prompt=summary_prompt_template)

    # res = chain.invoke(input={"information": information})
    # print(res)

    linkedin_data = scrape_linkedin_profile(
        # linkedin_profile_url="https://www.linkedin.com/in/jeegar-tilak-shah/"
        linkedin_profile_url=linkedin_profile_url
    )

    print(chain.run(information=linkedin_data))

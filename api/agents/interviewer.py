from crewai import Agent, Task, Crew
from api.config import get_llm
from api.schemas.interview import InterviewRequest, InterviewResponse

def run_mock_interview(request: InterviewRequest):
    """
    Run a mock interview with the specified parameters.

    Args:
        request: InterviewRequest
    
    Returns:
        InterviewResponse
    """

    print(request)

    # Get the LLM
    llm = get_llm()

    # Define the interviewer agent
    interviewer = Agent(
        role=f"""You are a technical interviewer for the {request.role} role at {request.company}.""",
        goal=f"""Conduct a mock interview with the candidate based on the job description as follows: {request.description}""",
        backstory="""You are a seasoned interviewer with a knack for asking challenging questions""",
        llm=llm
    )

    # Define the interview task
    task = Task(
        description=f"""Conduct a mock interview with the candidate based on the job description as follows: {request.description}""",
        expected_output="A list of 3 questions",
        agent=interviewer
    )

    # Create the crew
    crew = Crew(
        agents=[interviewer],
        tasks=[task],
        verbose=True
    )

    # Run the crew
    result = crew.kickoff()
    return result

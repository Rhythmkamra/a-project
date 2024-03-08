from django_workflow_engine import Step, Workflow

clerk_to_officer_workflow = Workflow(
    name="clerk_to_officer",
    steps=[
        Step(name="draft_message", description="Draft Message"),
        Step(name="review_message", description="Review Message"),
        Step(name="send_message", description="Send Message"),
        Step(name="receive_message", description="Receive Message"),
    ],
)

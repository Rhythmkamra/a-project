from django_workflow_engine import Step, Workflow

draft_step = Step(name="Draft", description="Draft Message")
approved_step = Step(name="Approved", description="Approved Message")
rejected_step = Step(name="Rejected", description="Rejected Message")


draft_step.add_transition(
    name="Approve",
    target_state=approved_step,
    description="Approve the Message",
)
draft_step.add_transition(
    name="Reject",
    target_state=rejected_step,
    description="Reject the Message",
)


message_workflow = Workflow(
    name="Message Workflow",
    initial_state=draft_step,
    states=[draft_step, approved_step, rejected_step],
)

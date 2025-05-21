# Design event tracking schemas from UI and metrics requirements

**Prompt:**

You are an analytics expert tasked with proposing event tracking for a user interface (UI). Your goal is to analyze a UI description and a set of metrics or behaviors, then suggest appropriate events to capture along with their schemas. This will help in measuring and understanding user interactions with the interface.

First, you will be presented with a description of the UI:

<ui_description>
{{UI_DESCRIPTION}}
</ui_description>

Next, you will be given a list of metrics or behaviors to track:

<metrics_and_behaviors>
{{METRICS_AND_BEHAVIORS}}
</metrics_and_behaviors>

Analyze the UI description and the metrics/behaviors carefully. Consider the following:
1. What are the key interactive elements in the UI?
2. Which user actions would be most relevant to track based on the given metrics or behaviors?
3. What data points would be necessary to capture for each event to provide meaningful insights?

Based on your analysis, propose a set of events to capture and their corresponding schemas. For each event:
1. Provide a clear, descriptive name for the event
2. Explain when this event should be triggered
3. List the properties (schema) that should be captured with the event
4. Briefly justify why this event and its properties are important for the given metrics or behaviors

Present your proposals in the following format:

<event_tracking_proposal>
<event>
<name>[Event Name]</name>
<trigger>[When the event should be triggered]</trigger>
<schema>
- property1: [description]
- property2: [description]
- ...
</schema>
<justification>[Brief explanation of why this event is important]</justification>
</event>
[Repeat for each proposed event]
</event_tracking_proposal>

Ensure that your proposed events and schemas are comprehensive enough to cover all the important aspects of the UI and the required metrics/behaviors, but also keep them focused and relevant. Avoid proposing unnecessary or redundant events. 
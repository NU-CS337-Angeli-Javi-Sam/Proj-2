from typing import List, Dict, Any

class DependencyParser:
    def __init__(self, beam_width: int = 3):
        self.beam_width = beam_width

    def parse(self, sentence: str) -> List[Dict["str", "str"]]:
        words = sentence.split()

        initial_state = {
            'stack': [],
            'buffer': words,
            'history': [],
            'score': 0.0  # You will need a scoring function.
        }
        beam = [initial_state]


        while beam:
            # Create a list to store new candidate states.
            new_beam = []

            for state in beam:
                # Generate a list of valid parsing actions for the current state.
                valid_actions = self.get_valid_actions(state)

                for action in valid_actions:
                    # Apply the action to create a new state.
                    new_state = self.apply_action(state, action)

                    # Calculate the score for the new state using a scoring function.
                    new_state['score'] = self.score_state(new_state)

                    # Add the new state to the candidate list.
                    new_beam.append(new_state)

            # Select the top-K states from the candidate list based on their scores.
            new_beam.sort(key=lambda x: x['score'], reverse=True)
            beam = new_beam[:self.beam_width]

        # Choose the best state as the final parsing result.
        best_state = max(beam, key=lambda x: x['score'])

        # Extract the dependency relations from the parsing history in the best state.
        dependencies = self.extract_dependencies(best_state['history'])

        return dependencies


    def get_valid_actions(self, state: Dict["str", Any]) -> List["str"]:
        valid_actions = []

        # The 'stack' and 'buffer' represent the current state of the parsing process.
        stack = state['stack']
        buffer = state['buffer']

        # You can consider adding 'shift' action as long as there are words in the buffer.
        if buffer:
            valid_actions.append('shift')

        # You can consider adding 'reduce' action if there are items on the stack.
        if stack:
            valid_actions.append('reduce')

        # You can consider adding 'left-arc' action if there are at least two items on the stack.
        if len(stack) >= 2:
            valid_actions.append('left-arc')

        # You can consider adding 'right-arc' action if there are at least two items on the stack.
        if len(stack) >= 2:
            valid_actions.append('right-arc')

        return valid_actions

    def apply_action(self, state: Dict["str", Any], action: str) -> Dict["str", Any]:
        # Make a copy of the current state to avoid modifying the original state.
        new_state = state.copy()

        # Get the stack, buffer, and history from the current state.
        stack = new_state['stack']
        buffer = new_state['buffer']
        history = new_state['history']

        if action == 'shift':
            # Apply the 'shift' action by moving the first word from the buffer to the stack.
            stack.append(buffer.pop(0))
        elif action == 'reduce':
            # Apply the 'reduce' action by removing the top item from the stack.
            stack.pop()
        elif action == 'left-arc':
            # Apply the 'left-arc' action by adding a dependency relation from the second item on the stack to the first.
            dependent = stack.pop()
            head = stack[-1]
            history.append(f'left-arc({head}, {dependent})')
        elif action == 'right-arc':
            # Apply the 'right-arc' action by adding a dependency relation from the first item on the stack to the second.
            head = stack.pop()
            dependent = stack[-1]
            history.append(f'right-arc({head}, {dependent})')

        # Update the state components in the new state.
        new_state['stack'] = stack
        new_state['buffer'] = buffer
        new_state['history'] = history

        return new_state

    def score_state(self, state: Dict["str", Any]) -> float:
        # Initialize the score to a base value.
        score = 0.0

        # You can define and add various features to the score based on the current state.
        # For instance, you can consider features related to the size of the stack, buffer, or history.
        # You might consider features that reflect how well the dependencies match linguistic patterns.

        # Example feature: Reward for the size of the stack (encouraging a smaller stack).
        stack_size = len(state['stack'])
        score += -0.1 * stack_size

        # Example feature: Reward for completed dependency relations in the history.
        completed_dependencies = state['history'].count("left-arc") + state['history'].count("right-arc")
        score += 0.5 * completed_dependencies

        return score

    def extract_dependencies(self, history: List["str"]) -> List[Dict["str", "str"]]:
        dependencies = []

        for action in history:
            # Split the action string into its components to extract dependency information.
            parts = action.split('(')
            if len(parts) == 2:
                relation, args = parts[0], parts[1][:-1]  # Remove the trailing parenthesis.

                if relation == 'left-arc':
                    head, dependent = args.split(', ')
                elif relation == 'right-arc':
                    dependent, head = args.split(', ')

                # Create a dictionary to represent the dependency relation and add it to the list.
                dependency = {'head': head, 'dependent': dependent, 'relation': relation}
                dependencies.append(dependency)

        return dependencies

from prototype.settings import text_settings
from prototype.text.message import Message
from prototype.text.text import Text
from core.shield.guard import Guard
from core.misc.range import Range

def take_integer_input(prompt: str, range: Range, custom_error_message: str | None = None) -> int:
    # Prompt
    message: Text = Text(text=prompt, decoration=text_settings['decoration']['prompt'])
    valid: bool = False
    data: int = 0

    # Take input
    while not valid:
        try:
            data = int(input(message))

            # Check validity
            try:
                Guard.against_out_of_range(range, data)
                valid = True
            except ValueError as e:
                Message.error(custom_error_message if custom_error_message else f'{e}')

        except Exception:
            Message.error('Input must be an integer.')
            continue

    return data

This script was used to edit directories on a staging server. There is room for standardization/optimization, but this was put together hastily to meet a deadline for a specific application.

This script iteratively writes commands for a java tool designed to interact with a staging server API. The iterative portion of the commands takes place in
the middle of the command, so two variables were written to capture the static portions of the command preceding and following the iterative portion of the command.

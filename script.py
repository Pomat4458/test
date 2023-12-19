import gradio as gr
import subprocess

def run_command(command):
    try:
        result = subprocess.run(command, shell=True, capture_output=True, text=True)
        return f"Result:\n{result.stdout}"
    except subprocess.CalledProcessError as e:
        return f"Error: {e.returncode}, {e.stderr}"

def command_interface(command):
    result = run_command(command)
    return result

iface = gr.Interface(
    fn=command_interface,
    inputs="text",
    outputs="text",
    live=True,
    title="Command Runner",
    description="Enter a command to run:",
)

iface.launch()

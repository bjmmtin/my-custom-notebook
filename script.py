from bs4 import BeautifulSoup

# Load the existing HTML file
input_file_path = 'dist/notebooks/index.html'
output_file_path = 'dist/notebooks/index.html'

with open(input_file_path, 'r', encoding='utf-8') as file:
    soup = BeautifulSoup(file, 'html.parser')

# Find the specific <script> tag to insert after
target_script = soup.find('script', text=lambda text: text and 'index.html' in text)

print(f'Modified HTML saved to ')
# Create the new script and style tags
new_script = '''
<script>
    function removeNotebookHeaders() {
        document.getElementById('top-panel-wrapper')?.remove();
        document.getElementById('menu-panel-wrapper')?.remove();
        document.getElementsByClassName('jp-NotebookPanel-toolbar')[0]?.remove();
    }

    function addChatInterface() {
        const addCell = document.querySelector('button.jp-Notebook-footer');
        addCell.style.marginBottom = "50px";

        const chatInterface = document.createElement('div');
        chatInterface.id = 'chat-interface';
        chatInterface.innerHTML = `
            <div class="chat-container">
                <input type="text" id="chat-input" placeholder="Type a message..." />
                <div style="display: flex; align-items: end; padding: 15px;">
                    <button class="send-button">
                        <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 384 512">
                            <path d="M214.6 41.4c-12.5-12.5-32.8-12.5-45.3 0l-160 160c-12.5 12.5-12.5 32.8 0 45.3s32.8 12.5 45.3 0L160 141.2 160 448c0 17.7 14.3 32 32 32s32-14.3 32-32l0-306.7L329.4 246.6c12.5 12.5 32.8 12.5 45.3 0s12.5-32.8 0-45.3l-160-160z"/>
                        </svg>
                    </button>
                </div>
            </div>
        `;
        addCell.parentNode.insertBefore(chatInterface, addCell.nextSibling);
    }

    function pollForHeaders() {
        if (document.querySelector('button.jp-Notebook-footer')) {
            removeNotebookHeaders();
            addChatInterface();
        } else {
            setTimeout(pollForHeaders, 50);
        }
    }

    // Start polling
    pollForHeaders();
</script>
'''

new_style = '''
<style>
    #chat-interface {
        position: fixed;
        left: 0;
        bottom: 0;
        width: calc(100% - 54px);
        background: transparent;
        margin: 0;
        padding: 0 20px 20px 20px;
        display: flex;
        justify-content: center;
        z-index: 10000;
    }

    .chat-container {
        display: flex;
        justify-content: space-between;
        max-width: 800px;
        background-color: #2f2c3d;
        border-radius: 30px;
        width: 100%;
        color: #d7d7dd;
        min-height: 100px;
    }

    #chat-input {
        border: 0;
        color: #d7d7dd;
        border-radius: 30px;
        background-color: #2f2c3d;
        max-width: calc(100vw - 20px);
        width: calc(100% - 150px);
        padding: 10px;
        margin: 0 10px;
        z-index: 100000;
    }

    input#chat-input::placeholder {
        color: #d7d7dd;
    }

    .send-button {
        border-radius: 50%;
        width: 30px;
        height: 30px;
        border: none;
        padding: 3px 6px 6px 6px;
    }
</style>
'''

# Insert the new script and style after the target script
target_script.insert_after(BeautifulSoup(new_style, 'html.parser'))
target_script.insert_after(BeautifulSoup(new_script, 'html.parser'))

# Save the modified HTML to a new file
with open(output_file_path, 'w', encoding='utf-8') as file:
    file.write(str(soup))

print(f'Modified HTML saved to {output_file_path}')

from string import Template

#Text Updater
class Update():
    changed_text = ""
    
    def __init__(self, text = None):
        self.text = text
        
    def get_text(self):
        return self.text
    
    def set_text(self, new_text):
        self.text = new_text

    def text_update(entered):
        pull = Update()
        pull.set_text(entered)
        result = pull.text
        template = Template("$text")
        text_string = template.safe_substitute(text = result)
        Update.changed_text = text_string
        

#Updating Text
def transform (entered):
    Update.text_update(entered)
    template = Template("$t_transformed")
    transformed_text = template.safe_substitute(t_transformed = Update.changed_text)
    
def paste_info(pre, text_variable):
    template2 = Template("$text")
    label_string = template2.safe_substitute(text = Update.changed_text)
    text_variable(pre + label_string)   

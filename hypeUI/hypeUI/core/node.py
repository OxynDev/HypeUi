import subprocess
import os

try:
    from core.setup import files
    from core.utils import react_to_signle
except:
    try:
        from setup import files
        from utils import react_to_signle
    except:
        from .setup import files
        from .utils import react_to_signle

class Project:
    def __init__(self):
        self.ui_dir_name = ".ui"
        self.old_dir = os.getcwd()
        self.check_node()
    
    def check_node(self):
        try:
            result = subprocess.run(['node', '-v'], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
            if result.returncode == 0:
                return True
            else:
                return False
                raise "Node.js is not installed."
        except FileNotFoundError:
            return False
            raise "Node.js is not installed."
    
    def init_ui(self):
        if not os.path.isdir(self.ui_dir_name):
            
            os.mkdir(self.ui_dir_name)
            os.chdir(self.ui_dir_name)
            
            subprocess.run("echo y | npm create vite@latest hypeui -- --template react -y", shell=True)
            
            os.chdir("hypeui")
            
            for cmd in (
                "npm install",
                "npm i @nextui-org/react framer-motion",
                "npm install -D tailwindcss postcss autoprefixer",
                "npx tailwindcss init -p",
                "npm install next-themes"
                ):
                
                subprocess.run(cmd, shell=True)
                print("Done: ", cmd)
                
            open("tailwind.config.js","w").write(files.tailwind_config)
            open("src/index.css","w").write(files.css)
            open("src/copy_css.css","w").write(files.css_app)
            open("src/App.css","w").write(files.css_app)
            open("src/main.jsx","w").write(files.main_jsx)
            open("src/App.jsx","w").write(files.app_jsx)
            open("src/copy_app.jsx","w").write(files.app_jsx)
            open("src/copy_main.jsx","w").write(files.app_jsx)
            open("index.html","w").write(files.html)
            
            os.chdir(self.old_dir)
            
            print("Init done")
    
    def build(self):
        
        os.chdir(self.ui_dir_name + "/hypeui/")
        subprocess.run("npm run build", shell=True)
        os.chdir(self.old_dir)
        
        return react_to_signle.inline_css_and_js_in_html(self.ui_dir_name + "/hypeui/dist/index.html", self.ui_dir_name)
    
    def process(self, 
                html: str, 
                imports: str, 
                js: str,
                css: str,
                svg_list
            ):

        if svg_list:
            for svg_data in svg_list:
                open(self.ui_dir_name + f"/hypeui/src/{svg_data[1]}.jsx", "w").write(svg_data[0])
                imports = imports + 'import {'+svg_data[1] +'} from "./'+svg_data[1]+'";' + "\n"
                
        app_jsx = open(self.ui_dir_name + "/hypeui/src/copy_app.jsx", "r").read()
        app_jsx = app_jsx.replace("// ||IMPORT||", imports)
        app_jsx = app_jsx.replace("{/* ||RETURN|| */}", html)
        app_jsx = app_jsx.replace("// ||CONTENT||", js)
        open(self.ui_dir_name + "/hypeui/src/App.jsx", "w").write(app_jsx)
        
        
        app_css = open(self.ui_dir_name + "/hypeui/src/copy_css.css", "r").read()
        app_css = app_css + "\n" + css
        open(self.ui_dir_name + "/hypeui/src/App.css", "w").write(app_css)
        
        one_file = self.build()
        return one_file
    
if __name__ == "__main__":
    project = Project()
    project.init_ui()
    project.build()
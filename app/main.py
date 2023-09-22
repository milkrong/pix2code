import os
from service import app

def main():
    app.config['ROOT_DIR'] = os.path.dirname(os.path.abspath(__file__))
    app.run(debug=True)

if __name__ == '__main__':
    main()
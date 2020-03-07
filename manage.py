from website import create_app

if __name__ == "__main__":
    app = create_app('test')
    app.run(port=app.config['PORT'])

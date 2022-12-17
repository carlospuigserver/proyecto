from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
  return render_template('index.html')

@app.route('/motocycles')
def motocycles():
  motocycles = ['Yamaha', 'Honda', 'Suzuki', 'Kawasaki']
  return render_template('motocycles.html', motocycles=motocycles)

if __name__ == '__main__':
  app.run()

pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                git url:'https://github.com/monika-sahay/frap.git', branch:'main'
            }
        }
        stage('Building Docker Image') {
            steps {
                sh 'docker build -t frap:1.0.0 .'
            }
        }
        stage('Linting') {
            steps {
                sh 'docker run --rm -v $PWD:/frap -w /frap frap:1.0.0 flake8 . --config=setup.cfg'
                sh 'docker run --rm -v $PWD:/frap -w /frap frap:1.0.0 pylint --rcfile=.pylintrc frap'
            }
        }
        stage('Testing') {
            steps {
                sh 'docker run --rm -p 8000:8000 -v $PWD:/frap -w /frap frap:1.0.0 bash -c "python3 run.py & pytest"'
            }
        }
        // stage('Building Distribution Package') {
        //     steps {
        //         sh 'docker run --rm -v $PWD:/frap -w /frap frap:1.0.0 python setup.py sdist bdist_wheel'
        //     }
        // }
        // stage('Upload to PyPI') {
        //     steps {
        //         sh 'docker run --rm -v $PWD:/frap -w /frap frap:1.0.0 twine upload dist/*'
        //     }
        // }

    }
}
pipeline {
    agent any
    stages{
        stage('Checkout') {
            steps {
                checkout scm
            }
        }
        stage('Test - install requirements') {
            steps {
                echo 'Installing requirements...'
            }
        }
        stage('Test - pytests') {
            steps {
                echo 'Runing unit tests...'
            }
        }
        stage('Submit Docker image build to CGP Cloud Build') {
            steps {
                echo 'Submitting docker image build...'
            }
        }
        stage('Deploy Cloud Run Service') {
            steps {
                echo 'Deploying Cloud Run Service...'
            }
        }
    }
    post{
        always{
            echo "======== Pipeline ends ========"
        }
        success{
            echo "======== Pipeline executed successfully ========"
        }
        failure{
            echo "======== Pipeline execution failed========"
        }
    }
}
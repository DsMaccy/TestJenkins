pipeline {
    agent any
    triggers {
        pollSCM '* * * * *'
    }
    stages {
        // NOTE: Checkout is implicit
        stage("Build") {
            steps {
                sh 'python3 -m py_compile main.py'
            }
        }
        stage("Test") {
            steps {
                sh 'py.test'
            }
        }
    }
    post {
        regression {
            emailext attachLog: true, body: '"An issue has occurred with the latest build', subject: 'Build Broken', to: 'dsmaccy@rocketmail.com'
            echo "An issue has occurred with the latest build"
            // One or more steps need to be included within each condition's block.
        }
        fixed {
            emailext attachLog: true, body: 'The previously broken build is now good', subject: 'Build Fixed', to: 'dsmaccy@rocketmail.com'
            echo 'The previously broken build is now good'
            // One or more steps need to be included within each condition's block.
        }
        changed {
            emailext attachLog: true, body: 'There is an anomolous new build status', subject: 'Build Status Changed', to: 'dsmaccy@rocketmail.com'
            echo "There is an anomolous new build status"
            // One or more steps need to be included within each condition's block.
        }
    }
}
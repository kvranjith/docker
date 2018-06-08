node {
    stage('Clone repository') {
        /* Let's make sure we have the repository cloned to our workspace */

        checkout scm
    }

    stage('Describe Instance') {
        /* This builds the actual image; synonymous to
         * docker build on the command line */

        sh 'python setup.py'

    }
}
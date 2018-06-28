node{
	def app
	def image = "ubuntu"
	def repo = "8kmilesranjith"
		
	stage('CLONE GIT'){
		checkout scm
	}
	stage('BUILD DOCKER'){
		sh "docker build -t ${repo}/${image}:${env.BUILD_NUMBER} ."
		
	}
	stage('RUN DOCKER'){
		sh "docker run ${repo}/${image}:${env.BUILD_NUMBER}" 
    }
	
	stage('Login Docker Hub'){
		
            sh "docker login -u 8kmilesranjith -p Vprema@3"
	
	}
	stage('PUSH IMAGE'){
		
            sh "docker push ${repo}/${image}:${env.BUILD_NUMBER}"
	
	}
	}
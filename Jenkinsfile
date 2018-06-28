node{
	def app
	def image = "ubuntu"
	def repo = "8kmilesranjith"
		
	stage('clone git Repo'){
		checkout scm
	}
	stage('docker build'){
		sh "docker build -t ${repo}/${image}:${env.BUILD_NUMBER} ."
		
	}
	stage('Run docker image'){
		sh "docker run ${repo}/${image}:${env.BUILD_NUMBER}" 
    }
	stage('push image'){
		sh "docker login -u 8kmilesranjith -p Vprema@3"
		sh "docker push ${repo}/${image}:${env.BUILD_NUMBER}"
	
	}
	}
node{
	def app
	def image = "ubuntu"
	def repo = "8kmilesranjith"
		
	stage('clone git Repo'){
		checkout scm
	}
	stage('docker build'){
		sh("docker build -t 8kmilesranjith/ubuntu .")
		app = docker.build("8kmilesranjith/ubuntu")
	}
	stage('Run docker image'){
		sh("docker run ${repo}/ubuntu go test")
    }
	}
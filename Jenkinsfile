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
	
	stage('PUSH IMAGE'){
	
            sh "docker login -u 8kmilesranjith -p Vprema@3 --email=k_vranjith@yahoo.co.in"
			sh "docker push ${repo}/${image}:${env.BUILD_NUMBER}"
			sh "docker push ${repo}/${image}:latest"
    
	}
	stage ('KUBERNETES CONNECTION'){
		withKubeConfig([credentialsId:'kubernetes',serverUrl:'https://api.k8s.kube.com'])
          {
          sh 'kubectl get pods --all-namespaces'
          sh 'kubectl get nodes -o wide'
          sh 'kubectl get svc --all-namespaces'
         }
		
	}
	stage('DEPLOY PODS'){
		withKubeConfig([credentialsId:'kubernetes',serverUrl:'https://api.k8s.kube.com'])
            {
            sh 'kubectl run pyt --image=8kmilesranjith/ubuntu:38 -it'
			}
	}
	}
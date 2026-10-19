FROM jenkins/jenkins:lts

USER root

# Instala kubectl + trivy + docker cli
RUN apt-get update && \
    apt-get install -y curl wget gnupg lsb-release apt-transport-https && \
    # kubectl
    curl -LO "https://dl.k8s.io/release/$(curl -L -s https://dl.k8s.io/release/stable.txt)/bin/linux/amd64/kubectl" && \
    install -o root -g root -m 0755 kubectl /usr/local/bin/kubectl && \
    rm kubectl && \
    # trivy
    wget -qO - https://aquasecurity.github.io/trivy-repo/deb/public.key | gpg --dearmor | tee /usr/share/keyrings/trivy.gpg > /dev/null && \
    echo "deb [signed-by=/usr/share/keyrings/trivy.gpg] https://aquasecurity.github.io/trivy-repo/deb generic main" | tee /etc/apt/sources.list.d/trivy.list && \
    apt-get update && apt-get install -y trivy docker.io && \
    apt-get clean && rm -rf /var/lib/apt/lists/*

# Permite jenkins usar docker.sock do host
RUN groupadd -g 999 docker || true && \
    usermod -aG docker jenkins && \
    chmod 666 /var/run/docker.sock || true 

USER jenkins

# Plugins úteis
RUN jenkins-plugin-cli --plugins kubernetes workflow-aggregator docker-workflow
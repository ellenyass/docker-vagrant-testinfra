
Vagrant.configure("2") do |config|

  # Sistema operacional da VM
  config.vm.box = "ubuntu/jammy64"

  # Nome da máquina
  config.vm.hostname = "web-server"

  # Encaminhamento SSH
  config.vm.network "forwarded_port",
    guest: 22,
    host: 2222,
    host_ip: "0.0.0.0"

  # Encaminhamento HTTP
  config.vm.network "forwarded_port",
    guest: 80,
    host: 8080

  # Configuração de recursos da VM
  config.vm.provider "virtualbox" do |vb|
    vb.name = "test-infra-web"
    vb.memory = 2048
    vb.cpus = 1
  end

end

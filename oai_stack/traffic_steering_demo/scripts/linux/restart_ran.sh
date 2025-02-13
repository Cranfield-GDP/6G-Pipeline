ue="$1"

if [[ "$ue" != "gnbsim-vpp" && "$ue" != "gnbsim-vpp2" ]]; then
    echo "Invalid arguments"
    exit 1
fi

echo "Stopping the RAN {$ue}"
docker compose -f docker-compose-ran-ue.yaml down "$ue"
sleep 1
docker compose -f docker-compose-ran-ue.yaml up "$ue" -d
echo "Restarted $ue successfully"
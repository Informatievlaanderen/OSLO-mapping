#use powershell
#make sure you have Rest installed so you can execute rest commands
#do this on an Aquafin laptop or connect to the network using VPN
#change the directory in powershell to github-repo-path/definitions


# Define the LDES datastream
Write-Host "Defining the LDES..."
Invoke-RestMethod -Method Post -Uri "https://ldes-overstort.test.az.aquafin.be/ldes/admin/api/v1/eventstreams" -ContentType "text/turtle" -InFile ".\overstort-event-cleansed.ttl"

# Wait to allow the previous step to finish
Start-Sleep -Seconds 5

# Define views for observation
Write-Host "Defining views..."
Invoke-RestMethod -Method Post -Uri "https://ldes-overstort.test.az.aquafin.be/ldes/admin/api/v1/eventstreams/overstort-event-cleansed/views" -ContentType "text/turtle" -InFile ".\overstort.overstort-event-cleansed-by-page.ttl"
Start-Sleep -Seconds 5


# Define pipelines
Write-Host "Defining pipelines..."
Invoke-RestMethod -Method Post -Uri "https://ldio-overstort.test.az.aquafin.be/admin/api/v1/pipeline" -ContentType "application/yaml" -InFile ".\overstort-event-cleansed.yaml"
Start-Sleep -Seconds 5


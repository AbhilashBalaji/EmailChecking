#live_a8979db0815b44775bfc8c15f51a92a6741bdde96cce8525e2e45101fa0741fa
import kickbox

client   = kickbox.Client('live_a8979db0815b44775bfc8c15f51a92a6741bdde96cce8525e2e45101fa0741fa')
kickbox  = client.kickbox()


response = kickbox.verify("Info1@inventureacademy.com")

print (response.body)

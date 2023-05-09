echo "start master..."
nohup locust -f sample230508.py --master --master-bind-port=8090 > ./log/main.log 2>&1 &

workerNum=3
echo "start worker, size=${workerNum}..."
for i in $( seq 1 ${workerNum})
do
  nohup locust -f sample230508.py --worker --master-host=172.16.88.11 --master-port=8090 > ./log/worker${i}.log 2>&1 &
  echo "output worker${i}.log"
done

echo "end..."

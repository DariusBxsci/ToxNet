python ./src/make_world.py
python ./src/make-train-db.py
python ./src/plot-distribution-of-cases.py

cp ./data/world-train.db ./world-train.db
cp ./data/world-test.db ./world-test.db
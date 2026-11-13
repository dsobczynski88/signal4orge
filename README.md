# signal4orge

A quarterly ridge ranker that scores stocks from five filing-date features, flags the weakest fifth, and refits only after those returns are realized.

Each company in a filing quarter is scored from information known on the filing date. The lowest fifth of scores is flagged as weak. The score stays pending until the next quarter's return is known. Completed quarters are then used to check the flag and to fit the next model.

The service stores filings, prices, scores, and realized outcomes in Postgres. FastAPI serves the current flag and the record of how those flags turned out.

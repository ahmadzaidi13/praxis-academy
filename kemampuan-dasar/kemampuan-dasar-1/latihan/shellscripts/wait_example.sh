#!/bin/bash
echo "harap bersabar" &
process_id=$!
wait $process_id
echo "selesai dengan status  $?"

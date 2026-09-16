# Exact certificate

`min_degree_7.json` contains two independent finite witnesses:

1. an 18-word polynomial of degree seven, to be checked on all 262144 ordered
   matrix pairs;
2. 15 ordered matrix pairs and 127 selected scalar coordinates whose degree-six
   word-evaluation minor has full rank 127 over F2.

The command

```bash
python3 src/verify_certificate.py certificates/min_degree_7.json
```

reconstructs matrix multiplication, the exhaustive identity check, the minor,
and all lower-degree ranks from the serialized integers. It does not import the
discovery implementation or NumPy/Numba.

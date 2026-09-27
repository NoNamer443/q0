s = 's = %r\nn = %d\nwith open(f"p{n + 1}.py", "w", encoding="UTF-8") as f:\n\tf.write(s %% (s, n + 1))'
n = 0
exec(s % (s, n))

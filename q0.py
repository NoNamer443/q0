s = 's = %r\nn = %d\nif n < 20:\n\twith open(f"p{n + 1}.py", "w", encoding="UTF-8") as f:\n\t\tf.write(s %% (s, n + 1))'
n = 0
exec(s % (s, n))
# Talon commands

from talon.voice import Context, Key
ctx = Context("text_plus_keys")
ctx.keymap(
    {
        "join remote server": Key("return"),
    }
)

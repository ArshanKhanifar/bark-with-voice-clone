from modal import Stub, Image, Mount

img = Image \
    .debian_slim()

stub = Stub("test-runner", image=img)


@stub.function(gpu="t4", mounts=[
    Mount.from_local_dir(
        "/Users/arshankhanifar/bark-with-voice-clone/voices",
        remote_path="/root/hello"
    )
])
def run_shit_in_gpu():
    with open("/root/hello/sometext", "r") as f:
        lines = f.readlines()
        lines = '\n'.join(lines)
        print(f"content:\n{lines}")


@stub.local_entrypoint()
def main():
    print("hello")
    run_shit_in_gpu.call()

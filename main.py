import cv2
from camera_dump import CameraDump
from load_config import load_config


def load_camera(camera_uri: str, camera_name: str, interval: float):
    frame_num: int = 0
    camera: CameraDump = CameraDump(camera_name=camera_name,
                                    camera_uri=camera_uri, interval=interval)

    while True:
        frame = camera.dump_frame()
        if frame is None:
            continue

        frame_num += 1
        frame = cv2.convertScaleAbs(frame, alpha=1, beta=60)
        cv2.imshow("Output Video", frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cv2.destroyAllWindows()


def main():
    camera_uri, camera_name, interval = load_config()
    load_camera(camera_uri=camera_uri,
                camera_name=camera_name, interval=interval)


if __name__ == '__main__':
    main()

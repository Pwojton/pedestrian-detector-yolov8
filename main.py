import cv2
from camera_dump import CameraDump
from load_config import load_config


def main():
    camera_uri, camera_name, interval = load_config()
    camera: CameraDump = CameraDump(camera_name=camera_name,
                                    camera_uri=camera_uri, interval=interval)
    frame_num: int = 0

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


if __name__ == '__main__':
    main()

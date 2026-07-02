"""
====================================================
VisionWork AI
Workforce Manager V2
====================================================
"""

from src.interfaces.manager import IManager
from src.models.employee import Employee


class WorkforceManager(IManager):

    def __init__(self):

        self.workforce = {}

        self.max_missing_frames = 30

    def update(self, tracks):

        active = set()

        if tracks is None:

            return {}

        if tracks.tracker_id is None:

            return {}

        for i in range(len(tracks.tracker_id)):

            track_id = tracks.tracker_id[i]

            if track_id is None:

                continue

            track_id = int(track_id)

            if track_id < 0:

                continue

            active.add(track_id)

            x1, y1, x2, y2 = map(int, tracks.xyxy[i])

            confidence = float(tracks.confidence[i])

            if track_id not in self.workforce:

                self.workforce[track_id] = Employee(

                    track_id=track_id,

                    bbox=(x1, y1, x2, y2),

                    confidence=confidence

                )

                self.workforce[track_id].missing = 0

            else:

                emp = self.workforce[track_id]

                emp.update_bbox(

                    (x1, y1, x2, y2)

                )

                emp.update_confidence(confidence)

                emp.missing = 0

                emp.status = "Present"

        remove = []

        for tid, emp in self.workforce.items():

            if tid not in active:

                emp.missing += 1

                if emp.missing > self.max_missing_frames:

                    remove.append(tid)

                else:

                    emp.status = "Absent"

        for tid in remove:

            del self.workforce[tid]

        return {

            tid: emp

            for tid, emp in self.workforce.items()

            if emp.status == "Present"

        }
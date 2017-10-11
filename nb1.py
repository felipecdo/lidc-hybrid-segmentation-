import os, warnings
import dicom
import numpy as np
import pylab

lidc_path = "/home/felipecdo/medical-imaging/images-TCIA/downloaded-images/DOI/"

class LidcSeries:
    patient =""
    study=""
    series=""
    folder_path=""
    dicom_image_paths=[]
    def add_image_path(self,image_path):
        self.dicom_image_paths.append(image_path)
    def __str__(self):
        return folder_path
    
    def read_dicom_image(self, position):
        with open(self.dicom_image_paths[position], 'rb') as f:
            return dicom.read_file(f)
        


def load_series(lidc_path, verbose=True):
    """
    Load all the DICOM images assocated with this scan and return as list.

    Example:
        >>> scan = pl.query(pl.Scan).first()
        >>> images = scan.load_all_dicom_images()
        >>> zs = [float(img.ImagePositionPatient[2]) for img in images]
        >>> print(zs[1] - zs[0], img.SliceThickness, scan.slice_thickness)
        >>>
        >>> import matplotlib.pyplot as plt
        >>> plt.imshow( images[0].pixel_array, cmap=plt.cm.gray )
        >>> plt.show()
    """
    if verbose: print("Loading dicom files ... This may take a moment.")

    path = lidc_path
    
    #"/patient_id/study_instance_uid/series_instance_uid"
    all_series = []
    
    for patient in os.listdir(path):
        for study in os.listdir(os.path.join(path,patient)):
            for series in os.listdir(os.path.join(path, patient, study)):
                lidcSerie = LidcSeries()
                folders = []        
                for folder_item in os.listdir(os.path.join(path, patient, study, series)):
                    if folder_item.endswith('.dcm'):
                        path_to_dicom = os.path.join(os.path.join(path, patient, study, series, folder_item))
                        folders.append(path_to_dicom )
                lidcSerie.patient = patient
                lidcSerie.study = study
                lidcSerie.series = series
                lidcSerie.dicom_image_paths = folders
                all_series.append(lidcSerie)
    
    if verbose: print("Series Count: " + str(len(all_series)))
    
    if verbose: print len(all_series[0].dicom_image_paths)
    if verbose: print len(all_series[1].dicom_image_paths)
    if verbose: print len(all_series[2].dicom_image_paths)
    if verbose: print len(all_series[7].dicom_image_paths)
    
    return all_series


series = load_series(lidc_path)
ds = series[0].read_dicom_image(0)
pylab.imshow(ds.pixel_array, cmap=pylab.cm.bone)
pylab.show()

print 'success'
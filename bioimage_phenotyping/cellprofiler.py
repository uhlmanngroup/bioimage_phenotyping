
BAD_COLS = [
    "Metadata_ChannelNumber_Organoid",
    "Metadata_FileLocation_Organoid",
    "Metadata_Frame_Organoid",
    "Metadata_Plate_Organoid",
    "Metadata_Series_Organoid",
    "Metadata_Site_Organoid",
    "Metadata_Well_Organoid",
    "Children_NucleiObjects_Count",
    "Number_Object_Number_Organoid",
    "Parent_NucleiObjectsPrimary",
    "Metadata_ChannelNumber_Nuclei",
    "Metadata_FileLocation_Nuclei",
    "Metadata_Frame_Nuclei",
    "Metadata_Plate_Nuclei",
    "Metadata_Series_Nuclei",
    "Metadata_Site_Nuclei",
    "Metadata_Well_Nuclei",
    "Metadata_ChannelNumber",
    "Metadata_FileLocation",
    "Metadata_Frame",
    "Metadata_Plate",
    "Metadata_Series",
    "Metadata_Site",
    "Metadata_Well",
    "Channel_Channels",
    "Count_MergedCellObjects",
    "Count_NucleiObjects",
    "Count_NucleiObjectsPrimary",
    "ExecutionTime_01Images",
    "ExecutionTime_02Metadata",
    "ExecutionTime_03NamesAndTypes",
    "ExecutionTime_04Groups",
    "ExecutionTime_05ColorToGray",
    "ExecutionTime_06RescaleIntensity",
    "ExecutionTime_07IdentifyPrimaryObjects",
    "ExecutionTime_08SplitOrMergeObjects",
    "ExecutionTime_09IdentifyPrimaryObjects",
    "ExecutionTime_10RelateObjects",
    "ExecutionTime_11MeasureObjectIntensity",
    "ExecutionTime_12MeasureObjectSizeShape",
    "ExecutionTime_13MeasureGranularity",
    "ExecutionTime_14MeasureTexture",
    "ExecutionTime_15MeasureImageAreaOccupied",
    "ExecutionTime_19OverlayOutlines",
    "ExecutionTime_20SaveImages",
    "ExecutionTime_17MeasureGranularity",
    "FileName_Channels",
    "FileName_OrigOverlay",
    "Frame_Channels",
    "Group_Index",
    "Group_Number",
    "Height_Channels",
    "ImageSet_ImageSet",
    "MD5Digest_Channels",
    "Metadata_ChannelNumber",
    "Metadata_FileLocation",
    "Metadata_Frame",
    "Metadata_Plate",
    "Metadata_Series",
    "Metadata_Site",
    "Metadata_Well",
    "ModuleError_01Images",
    "ModuleError_02Metadata",
    "ModuleError_03NamesAndTypes",
    "ModuleError_04Groups",
    "ModuleError_05ColorToGray",
    "ModuleError_06RescaleIntensity",
    "ModuleError_07IdentifyPrimaryObjects",
    "ModuleError_08SplitOrMergeObjects",
    "ModuleError_09IdentifyPrimaryObjects",
    "ModuleError_10RelateObjects",
    "ModuleError_11MeasureObjectIntensity",
    "ModuleError_12MeasureObjectSizeShape",
    "ModuleError_13MeasureGranularity",
    "ModuleError_14MeasureTexture",
    "ModuleError_15MeasureImageAreaOccupied",
    "ModuleError_19OverlayOutlines",
    "ModuleError_20SaveImages",
    "PathName_Channels",
    "PathName_OrigOverlay",
    "ProcessingStatus",
    "Scaling_Channels",
    "Series_Channels",
    "URL_Channels",
    "URL_OrigOverlay",
    "Width_Channels",
    "Metadata_C",
    "Metadata_SizeC",
    "Metadata_SizeT",
    "Metadata_SizeX",
    "Metadata_SizeY",
    "Metadata_SizeZ",
    "Metadata_Z",
    "Channel_Raw",
    "Channel_background",
    "Channel_nuclei_border",
    "Channel_nuclei_mask",
    "Count_nuclei_mask_borders_scaled_object",
    "Count_nuclei_mask_scaled_object",
    "ExecutionTime_05RescaleIntensity",
    "ExecutionTime_07RescaleIntensity",
    "ExecutionTime_08RescaleIntensity",
    "ExecutionTime_09ImageMath",
    "ExecutionTime_10RescaleIntensity",
    "ExecutionTime_11IdentifyPrimaryObjects",
    "ExecutionTime_12IdentifySecondaryObjects",
    "ExecutionTime_14MeasureObjectIntensity",
    "ExecutionTime_15MeasureObjectSizeShape",
    "ExecutionTime_16MeasureGranularity",
    "ExecutionTime_17MeasureTexture",
    "ExecutionTime_18MeasureImageAreaOccupied",
    "ExecutionTime_19MeasureImageQuality",
    "ExecutionTime_23OverlayOutlines",
    "ExecutionTime_24Tile",
    "ExecutionTime_25SaveImages",
    "ExecutionTime_26SaveImages",
    "Frame_Raw",
    "Frame_background",
    "Frame_nuclei_border",
    "Frame_nuclei_mask",
    "Height_Raw",
    "Height_background",
    "Height_nuclei_border",
    "Height_nuclei_mask",
    "Metadata_C_Image",
    "Metadata_Series_Image",
    "Metadata_SizeC_Image",
    "Metadata_SizeT_Image",
    "Metadata_SizeX_Image",
    "Metadata_SizeY_Image",
    "Metadata_SizeZ_Image",
    "Metadata_Z_Image",
    "ModuleError_05RescaleIntensity",
    "ModuleError_07RescaleIntensity",
    "ModuleError_08RescaleIntensity",
    "ModuleError_09ImageMath",
    "ModuleError_10RescaleIntensity",
    "ModuleError_11IdentifyPrimaryObjects",
    "ModuleError_12IdentifySecondaryObjects",
    "ModuleError_14MeasureObjectIntensity",
    "ModuleError_15MeasureObjectSizeShape",
    "ModuleError_16MeasureGranularity",
    "ModuleError_17MeasureTexture",
    "ModuleError_18MeasureImageAreaOccupied",
    "ModuleError_19MeasureImageQuality",
    "ModuleError_23OverlayOutlines",
    "ModuleError_24Tile",
    "ModuleError_25SaveImages",
    "ModuleError_26SaveImages",
    "Scaling_Raw",
    "Scaling_background",
    "Scaling_nuclei_border",
    "Scaling_nuclei_mask",
    "Series_Raw",
    "Series_background",
    "Series_nuclei_border",
    "Series_nuclei_mask",
    "Channel_Raw",
    "Channel_background",
    "Channel_nuclei_border",
    "Channel_nuclei_mask",
    "Count_nuclei_mask_borders_scaled_object",
    "Count_nuclei_mask_scaled_object",
    "ExecutionTime_05RescaleIntensity",
    "ExecutionTime_07RescaleIntensity",
    "ExecutionTime_08RescaleIntensity",
    "ExecutionTime_09ImageMath",
    "ExecutionTime_10RescaleIntensity",
    "ExecutionTime_11IdentifyPrimaryObjects",
    "ExecutionTime_12IdentifySecondaryObjects",
    "ExecutionTime_14MeasureObjectIntensity",
    "ExecutionTime_15MeasureObjectSizeShape",
    "ExecutionTime_16MeasureGranularity",
    "ExecutionTime_17MeasureTexture",
    "ExecutionTime_18MeasureImageAreaOccupied",
    "ExecutionTime_19MeasureImageQuality",
    "ExecutionTime_23OverlayOutlines",
    "ExecutionTime_24Tile",
    "ExecutionTime_25SaveImages",
    "ExecutionTime_26SaveImages",
    "Frame_Raw",
    "Frame_background",
    "Frame_nuclei_border",
    "Frame_nuclei_mask",
    "Height_Raw",
    "Height_background",
    "Height_nuclei_border",
    "Height_nuclei_mask",
    "Metadata_C_Image",
    "Metadata_Series_Image",
    "Metadata_SizeC_Image",
    "Metadata_SizeT_Image",
    "Metadata_SizeX_Image",
    "Metadata_SizeY_Image",
    "Metadata_SizeZ_Image",
    "Metadata_Z_Image",
    "ModuleError_05RescaleIntensity",
    "ModuleError_07RescaleIntensity",
    "ModuleError_08RescaleIntensity",
    "ModuleError_09ImageMath",
    "ModuleError_10RescaleIntensity",
    "ModuleError_11IdentifyPrimaryObjects",
    "ModuleError_12IdentifySecondaryObjects",
    "ModuleError_14MeasureObjectIntensity",
    "ModuleError_15MeasureObjectSizeShape",
    "ModuleError_16MeasureGranularity",
    "ModuleError_17MeasureTexture",
    "ModuleError_18MeasureImageAreaOccupied",
    "ModuleError_19MeasureImageQuality",
    "ModuleError_23OverlayOutlines",
    "ModuleError_24Tile",
    "ModuleError_25SaveImages",
    "ModuleError_26SaveImages",
    "Scaling_Raw",
    "Scaling_background",
    "Scaling_nuclei_border",
    "Scaling_nuclei_mask",
    "Series_Raw",
    "Series_background",
    "Series_nuclei_border",
    "Series_nuclei_mask",
    "Width_Raw",
    "Width_background",
    "Width_nuclei_border",
    "Width_nuclei_mask",
    "Intensity_UpperQuartileIntensity_Raw_scaled",
    "Location_CenterMassIntensity_X_Raw_scaled",
    "Location_CenterMassIntensity_Y_Raw_scaled",
    "Location_CenterMassIntensity_Z_Raw_scaled",
    "Location_Center_X",
    "Location_Center_Y",
    "Location_Center_Z",
    "Location_MaxIntensity_X_Raw_scaled",
    "Location_MaxIntensity_Y_Raw_scaled",
    "Location_MaxIntensity_Z_Raw_scaled",
    "Number_Object_Number",
    "Channel_Raw",
    "Channel_background",
    "Channel_nuclei_border",
    "Channel_nuclei_mask",
    "Count_nuclei_mask_borders_scaled_object",
    "Count_nuclei_mask_scaled_object",
    "ExecutionTime_05RescaleIntensity",
    "ExecutionTime_07RescaleIntensity",
    "ExecutionTime_08RescaleIntensity",
    "ExecutionTime_09ImageMath",
    "ExecutionTime_10RescaleIntensity",
    "ExecutionTime_11IdentifyPrimaryObjects",
    "ExecutionTime_12IdentifySecondaryObjects",
    "ExecutionTime_14MeasureObjectIntensity",
    "ExecutionTime_15MeasureObjectSizeShape",
    "ExecutionTime_16MeasureGranularity",
    "ExecutionTime_17MeasureTexture",
    "ExecutionTime_18MeasureImageAreaOccupied",
    "ExecutionTime_19MeasureImageQuality",
    "ExecutionTime_23OverlayOutlines",
    "ExecutionTime_24Tile",
    "ExecutionTime_25SaveImages",
    "ExecutionTime_26SaveImages",
    "Frame_Raw",
    "Frame_background",
    "Frame_nuclei_border",
    "Frame_nuclei_mask",
    "ExecutionTime_01Images",
    "ExecutionTime_02Metadata",
    "ExecutionTime_03NamesAndTypes",
    "ExecutionTime_04Groups",
    "ExecutionTime_06RescaleIntensity",
    "ExecutionTime_13MeasureGranularity",
    "ExecutionTime_14MeasureImageAreaOccupied",
    "ExecutionTime_15MeasureImageIntensity",
    "ExecutionTime_17MeasureImageQuality",
    "ExecutionTime_19MeasureObjectIntensity",
    "ExecutionTime_20MeasureObjectIntensityDistribution",
    "ExecutionTime_23MeasureObjectSizeShape",
    "ExecutionTime_26MeasureTexture"
]
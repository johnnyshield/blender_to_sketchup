import bpy
import os

bl_info = {
 "name": "Collada Exporter",
 "description": "Tool to batch export dae files",
 "author": "Patrick Jezek, Johnny Shield",
 "blender": (2, 7, 5),
 "version": (1, 0, 0),
 "category": "Export",
 "location": "",
 "warning": "",
 "wiki_url": "",
 "tracker_url": "",
}


class ColladaBatchExportPanel(bpy.types.Panel):

    bl_idname = "Collada_Exporter"
    bl_label = "Collada Exporter"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'TOOLS'
    bl_context = "objectmode"
    bl_options = {'DEFAULT_CLOSED'}

    def draw(self, context):

        layout = self.layout

        # batch export
        col = layout.column(align=True)
        col.label(text="Batch export:")
        col.prop(context.scene, 'pea_batch_export_path')
        row = col.row(align=True)
        row.operator("pea.batch_export", text="Batch Export", icon='EXPORT')

class PeaBatchExport(bpy.types.Operator):
    bl_idname = "pea.batch_export"
    bl_label = "Choose Directory"

    def execute(self, context):
        print ("execute Pea_batch_export")

        basedir = os.path.dirname(bpy.data.filepath)
        if not basedir:
            raise Exception("Blend file is not saved")

        if context.scene.pea_batch_export_path == "":
            raise Exception("Export path not set")

        # select all visible meshes
        mesh=[]
        bpy.ops.object.select_all(action='DESELECT')
        bpy.ops.object.select_by_type(type='MESH')
        col = bpy.context.selected_objects

        # convert path to windows friendly notation
        dir = os.path.dirname(bpy.path.abspath(context.scene.pea_batch_export_path))
        # cursor to origin
        bpy.context.scene.cursor_location = (0.0, 0.0, 0.0)

        for obj in col:
            # select only current object
            bpy.ops.object.select_all(action='DESELECT')
            obj.select = True
            # freeze location, rotation and scale
            bpy.ops.object.transform_apply(location=True, rotation=True, scale=True)
            # set pivot point to cursor location
            # Commented out by JS for DAE export
            # bpy.ops.object.mode_set(mode='OBJECT')
            bpy.ops.object.origin_set(type='ORIGIN_CURSOR')
            # store mesh
            mesh.append(obj)
            # use mesh name for file name
            name = bpy.path.clean_name(obj.name)
            fn = os.path.join(dir, name)
            print("exporting: " + fn)
            # export dae
            bpy.ops.wm.collada_export(filepath=fn + ".dae", selected=True, triangulate=True)
           
            # export 3ds
            # bpy.ops.export_scene.autodesk_3ds(filepath=fn + ".3ds", axis_forward='-Z', axis_up='Y')

        return {'FINISHED'}

# registers
def register():
    bpy.types.Scene.pea_batch_export_path = bpy.props.StringProperty (
        name="Export Path",
        default="",
        description="Define the path where to export",
        subtype='DIR_PATH'
    )
    bpy.utils.register_class(ColladaBatchExportPanel)
    bpy.utils.register_class(PeaBatchExport)


def unregister():
    del bpy.types.Scene.pea_batch_export_path
    bpy.utils.unregister_class(ColladaBatchExportPanel)
    bpy.utils.unregister_class(PeaBatchExport)


if __name__ == "__main__":
    register()
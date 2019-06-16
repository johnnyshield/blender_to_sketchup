import bpy
import os

bl_info = {
 "name": "Batch Collada Exporter",
 "description": "Tool to batch export dae files",
 "author": "Patrick Jezek, edited by Johnny Shield",
 "blender": (2, 80, 0),
 "version": (1, 0, 4),
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
    # Changed Tools to UI for 2.80
    bl_region_type = "UI"
    # Added so not under Misc
    bl_category = "View"
    bl_context = "objectmode"
    bl_options = {'DEFAULT_CLOSED'}

    def draw(self, context):

        layout = self.layout

        # batch export
        col = layout.column(align=True)
        col.label(text="Batch export to folder")
        col.prop(context.scene, 'collada_batch_export_path')
        row = col.row(align=True)
        row.operator("collada.batch_export", text="Batch Export", icon='EXPORT')

class ColladaBatchExport(bpy.types.Operator):
    bl_idname = "collada.batch_export"
    bl_label = "Choose Directory"

    def execute(self, context):
        print ("execute Collada_batch_export")

        basedir = os.path.dirname(bpy.data.filepath)
        if not basedir:
            raise Exception("Blend file is not saved")

        if context.scene.collada_batch_export_path == "":
            raise Exception("Export path not set")

        # select all visible meshes
        mesh=[]
        bpy.ops.object.select_all(action='DESELECT')
        bpy.ops.object.select_by_type(type='MESH')
        col = bpy.context.selected_objects

        # convert path to windows friendly notation
        dir = os.path.dirname(bpy.path.abspath(context.scene.collada_batch_export_path))
        # cursor to origin
        bpy.context.scene.cursor_location = (0.0, 0.0, 0.0)

        for obj in col:
            # select only current object
            bpy.ops.object.select_all(action='DESELECT')
            # Updated for 2.80 from obj.select = True
            obj.select_set(True)
            # freeze location, rotation and scale
            bpy.ops.object.transform_apply(location=True, rotation=True, scale=True)
            # set pivot point to cursor location
            # Check if this is needed - commented out by JS in 2.79 for DAE export
            bpy.ops.object.mode_set(mode='OBJECT')
            bpy.ops.object.origin_set(type='ORIGIN_CURSOR')
            # store mesh
            mesh.append(obj)
            # use mesh name for file name
            name = bpy.path.clean_name(obj.name)
            fn = os.path.join(dir, name)
            print("exporting: " + fn)
            # export dae
            bpy.ops.wm.collada_export(filepath=fn + ".dae", selected=True, triangulate=True)
        return {'FINISHED'}

# registers
def register():
    bpy.types.Scene.collada_batch_export_path = bpy.props.StringProperty (
        name="Export Path",
        default="",
        description="Define the path where to export",
        subtype='DIR_PATH'
    )
    bpy.utils.register_class(ColladaBatchExportPanel)
    bpy.utils.register_class(ColladaBatchExport)


def unregister():
    del bpy.types.Scene.collada_batch_export_path
    bpy.utils.unregister_class(ColladaBatchExportPanel)
    bpy.utils.unregister_class(ColladaBatchExport)


if __name__ == "__main__":
    register()
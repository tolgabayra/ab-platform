'use client'
import { Box, Grid } from '@mui/material'
import React from 'react'

type Props = {}

export default function Deneme({ }: Props) {
    return (
        <div>

            <Box>
                <Grid container spacing={0}>
                    {/* ------------------------- row 1 ------------------------- */}
                    <Grid item xs={12} lg={12}>
                        fdsfgsd
                    </Grid>
                    {/* ------------------------- row 2 ------------------------- */}
                    <Grid item xs={12} lg={4}>
                        fsdfdsfds
                    </Grid>
                    <Grid item xs={12} lg={8}>
                        dfsf
                    </Grid>
                    {/* ------------------------- row 3 ------------------------- */}
                    fdsfsd
                </Grid>
            </Box>
        </div>
    )
}